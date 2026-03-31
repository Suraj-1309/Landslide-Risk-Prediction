import { Navigate, Route, Routes } from "react-router-dom";
import DatasetPage from "../../features/dataset/pages/DatasetPage";

function HomePage(){
    return(
        <section className="mx-auto mx-w-7xl px-4 py-6 sm:px-6 lg:px-8">
            <h1 className="text-2xl font-semibold text-slate-900">Home</h1>
            <p className="mt-2 text-slate-600">Welcome to Landslide Predictor</p>
        </section>
    );
}

export default function AppRoutes(){
    return(
        <Routes>
            <Route path="/" element={<HomePage />}/>
            <Route path="/dataset" element={<DatasetPage />}/>
            <Route path="*" element={<Navigate to="/" replace />}/>
        </Routes>
    )
}