function getSpaceData(spaceId) {
    fetch(`/spaces/ajax/${spaceId}/`)  // 🔹 Llama a la vista AJAX
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();  // 🔹 Convierte la respuesta a JSON
    })
    .then(data => {
        console.log("Datos recibidos:", data);
        // Aquí puedes actualizar tu HTML con los datos recibidos
    })
    .catch(error => {
        console.error("Error en la solicitud AJAX:", error);
    });
}