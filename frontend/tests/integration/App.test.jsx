
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { afterEach, expect, it, vi } from "vitest";
import App from "../../src/App";

afterEach(() => {
  vi.unstubAllGlobals();
});

it("cadastra um item e o exibe na lista", async () => {
  const user = userEvent.setup();

  const newItem = {
    id: 1,
    name: "Notebook",
    description: "14 polegadas",
  };

    const fetchMock = vi.fn(async (_url, options = {}) => {
    if (options.method === "POST") {
      return {
        ok: true,
        json: async () => newItem,
      };
    }

    return {
      ok: true,
      json: async () => [],
    };
  });

  vi.stubGlobal("fetch", fetchMock);

  render(<App />);

  await user.type(screen.getByLabelText("Nome"), "Notebook");
  await user.type(screen.getByLabelText("Descrição"), "14 polegadas");

  await user.click(screen.getByRole("button", { name: "Adicionar" }));

  expect(
    await screen.findByRole("heading", { name: "Notebook" }),
  ).toBeInTheDocument();

  expect(screen.getByText("14 polegadas")).toBeInTheDocument();

  expect(fetchMock).toHaveBeenCalledWith(
    expect.stringContaining("/items"),
    expect.objectContaining({
      method: "POST",
      body: JSON.stringify({
        name: "Notebook",
        description: "14 polegadas",
      }),
    }),
  );
});

it("exibe uma mensagem enquanto carrega os itens", () => {
  const fetchMock = vi.fn(() => new Promise(() => {}));

  vi.stubGlobal("fetch", fetchMock);

  render(<App />);

  expect(screen.getByRole("status")).toHaveTextContent(
    "Carregando itens...",
  );
});

it("exibe uma mensagem quando ocorre erro ao carregar os itens", async () => {
  const fetchMock = vi.fn(() =>
    Promise.reject(new Error("Falha ao carregar itens.")),
  );

  vi.stubGlobal("fetch", fetchMock);

  render(<App />);

  expect(await screen.findByRole("alert")).toHaveTextContent(
    "Falha ao carregar itens.",
  );

  expect(
    screen.getByRole("button", { name: "Tentar novamente" }),
  ).toBeInTheDocument();
});
