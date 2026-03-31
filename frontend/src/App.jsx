import AppRoutes from "./app/routes/routes";
import Navbar from "./components/layout/Navbar";

function App() {
  return (
    <div className="min-h-screen bg-slate-50">
      <Navbar />
      <AppRoutes/>
    </div>
  );
}

export default App;
