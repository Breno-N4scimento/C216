const API_URL = (
  import.meta.env.VITE_API_URL || "http://localhost:8000"
).replace(/\/$/, "");

async function handleResponse(response) {
  if (!response.ok) {
    let message = "Não foi possível concluir a operação.";

    try {
      const data = await response.json();
      message = typeof data.detail === "string" ? data.detail : message;
    } catch {
      // Mantém a mensagem padrão.
    }

    throw new Error(message);
  }

  if (response.status === 204) {
    return null;
  }

  return response.json();
}

export async function listItems() {
  const response = await fetch(`${API_URL}/items`);
  return handleResponse(response);
}

export async function createItem(item) {
  const response = await fetch(`${API_URL}/items`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(item),
  });

  return handleResponse(response);
}

export async function deleteItem(id) {
  const response = await fetch(`${API_URL}/items/${id}`, {
    method: "DELETE",
  });

  return handleResponse(response);
}
