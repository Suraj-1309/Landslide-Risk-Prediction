import Navbar from "./components/layout/Navbar";

function App() {
  return (
    <div className="min-h-screen bg-slate-50">
      <Navbar />
      <div className="min-h-screen bg-gradient-to-r from-blue-400 to-purple-500 flex items-center justify-center">
      <div className="bg-white rounded-lg shadow-xl p-8 max-w-md">
        <h1 className="text-3xl font-bold text-gray-800 mb-4">🎉 Tailwind CSS is Working!</h1>
        <p className="text-gray-600 mb-6">Your React + Tailwind setup is complete.</p>
        <button className="w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded transition-colors">
          Get Started
        </button>
      </div>
    </div>
    </div>
  );
}

export default App;
