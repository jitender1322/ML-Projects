import { useRef, useState } from "react";
import api from "./services/api";

function App() {

  const mediaRecorderRef = useRef(null);

  const [isRecording, setIsRecording] = useState(false);

  const [loading, setLoading] = useState(false);

  const [result, setResult] = useState(null);

  const [audioURL, setAudioURL] = useState(null);

  // START RECORDING
  const startRecording = async () => {

    try {



      const stream = await navigator.mediaDevices.getUserMedia({
        audio: true,
      });

      console.log(
  MediaRecorder.isTypeSupported(
    "audio/webm;codecs=opus"
  )
);
      const mediaRecorder = new MediaRecorder(stream, {
        mimeType: "audio/webm;codecs=opus",
      });

      mediaRecorderRef.current = mediaRecorder;

      const chunks = [];

      // collect audio chunks
      mediaRecorder.ondataavailable = (event) => {

        if (event.data.size > 0) {
          chunks.push(event.data);
        }
      };

      // when recording stops
      mediaRecorder.onstop = async () => {

        const audioBlob = new Blob(chunks, {
          type: "audio/webm",
        });

        console.log("Audio Blob Size:", audioBlob.size);

        // DEBUG
        if (audioBlob.size === 0) {
          alert("Audio recording failed");
          return;
        }

        // create local playback url
        const url = URL.createObjectURL(audioBlob);

        setAudioURL(url);

        // upload audio
        await uploadAudio(audioBlob);

        // stop microphone tracks
        stream.getTracks().forEach((track) => track.stop());
      };

      // start recording
      mediaRecorder.start();

      setIsRecording(true);

    } catch (error) {

      console.error("Microphone Error:", error);
    }
  };

  // STOP RECORDING
  const stopRecording = () => {

    if (mediaRecorderRef.current) {

      mediaRecorderRef.current.stop();

      setIsRecording(false);
    }
  };

  // UPLOAD AUDIO
  const uploadAudio = async (audioBlob) => {

    try {

      setLoading(true);

      const formData = new FormData();

      formData.append(
        "audio",
        audioBlob,
        "recording.webm"
      );

      const response = await api.post(
        "/api/speech/upload",
        formData
      );

      console.log("Backend Response:", response.data);

      setResult(response.data);

    } catch (error) {

      console.error("Upload Error:", error);

    } finally {

      setLoading(false);
    }
  };

  return (

    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-6">

      <h1 className="text-4xl font-bold mb-8 text-blue-600">
        SpeakUp AI
      </h1>

      {/* RECORD BUTTONS */}
      <div className="flex gap-4">

        {!isRecording ? (

          <button
            onClick={startRecording}
            className="bg-green-500 hover:bg-green-600 text-white px-6 py-3 rounded-lg"
          >
            Start Recording
          </button>

        ) : (

          <button
            onClick={stopRecording}
            className="bg-red-500 hover:bg-red-600 text-white px-6 py-3 rounded-lg"
          >
            Stop Recording
          </button>

        )}

      </div>

      {/* LOADING */}
      {loading && (

        <p className="mt-6 text-lg font-semibold">
          Processing audio...
        </p>

      )}

      {/* AUDIO PLAYER */}
      {audioURL && (

        <div className="mt-6">

          <audio controls src={audioURL} />

        </div>
      )}

      {/* RESULTS */}
      {result?.data && (

        <div className="bg-white shadow-lg rounded-xl p-6 mt-8 w-full max-w-2xl">

          <h2 className="text-2xl font-bold mb-4">
            Analysis Result
          </h2>

          <p className="mb-3">
            <strong>Original:</strong>{" "}
            {result.data.original_text || "No speech detected"}
          </p>

          <p className="mb-3">
            <strong>Corrected:</strong>{" "}
            {result.data.corrected_text || "No correction available"}
          </p>

          <p className="mb-3">
            <strong>Fluency Score:</strong>{" "}
            {result.data.fluency_score}/10
          </p>

          <div>

            <strong>Grammar Feedback:</strong>

            {result.data.grammar_feedback.length === 0 ? (

              <p className="mt-2 text-gray-600">
                No grammar mistakes found.
              </p>

            ) : (

              <ul className="list-disc ml-6 mt-2">

                {result.data.grammar_feedback.map(
                  (item, index) => (

                    <li key={index}>
                      "{item.wrong}" → "{item.correct}"
                    </li>

                  )
                )}

              </ul>

            )}

          </div>

        </div>
      )}

    </div>
  );
}

export default App;