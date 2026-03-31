import { API_BASE_URL } from "../../config/env";

export async function httpGet(path) {
    const response = await fetch(`${API_BASE_URL}${path}`);

    if(!response.ok){
        const text = await response.text();
        throw new Error(text || `Request failed with status ${response.status}`)
    }
    return response.json();
}
