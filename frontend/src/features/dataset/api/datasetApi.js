import { API_BASE_URL } from "../../../config/env";
import { httpGet } from "../../../services/http/client";

export function getDataset(){
    return httpGet("/api/v1/data");
}

export function getDownloadUrl(format = "csv"){
    return `${API_BASE_URL}/api/v1/data/download?format=${format}`;
}

export function getCsvDownloadUrl(){
    return getDownloadUrl("csv");
}

export function getJsonDownloadUrl(){
    return getDownloadUrl("json");
}

export function getXlsxDownloadUrl(){
    return getDownloadUrl("xlsx");
}

