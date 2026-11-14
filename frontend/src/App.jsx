
import { useCallback, useEffect, useState } from "react";
import { ItemForm } from "./components/ItemForm";
import { ItemList } from "./components/ItemList";
import {
  createItem,
  deleteItem,
  listItems,
} from "./services/items";

export default function App() {
  const [items, setItems] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState("");

  const loadItems = useCallback(async () => {
    setIsLoading(true);
    setError("");

    try {
      const data = await listItems();
      setItems(data);
    } catch (error) {
      setError(error.message || "Não foi possível carregar os itens.");
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    loadItems();
  }, [loadItems]);

  async function addItem(item) {
    const newItem = await createItem(item);

    setItems((currentItems) => [newItem, ...currentItems]);
  }

  async function removeItem(id) {
    try {
      await deleteItem(id);
      setItems((currentItems) =>
        currentItems.filter((item) => item.id !== id),
      );
      setError("");
    } catch (error) {
      setError(error.message || "Não foi possível excluir o item.");
    }
  }

  return (
    <main className="min-h-screen bg-slate-100 px-4 py-8 text-slate-800 sm:px-8">
      <div className="mx-auto max-w-5xl">
        <header className="mb-8 rounded-2xl bg-blue-700 p-6 text-white shadow-sm">
          <p className="text-sm text-blue-100">Painel de controle</p>
          <h1 className="mt-2 text-3xl font-bold">Gerenciador de Itens</h1>
          <p className="mt-2 text-sm text-blue-100">
            Cadastre, consulte e gerencie seus registros.
          </p>
        </header>

        <section
          aria-label="Resumo dos itens"
          className="mb-8 grid gap-4 sm:grid-cols-2"
        >
          <article className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
            <p className="text-sm text-slate-500">Total de itens</p>
            <p className="mt-2 text-3xl font-bold">{items.length}</p>
          </article>

          <article className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
            <p className="text-sm text-slate-500">Status</p>
            <p className="mt-2 text-xl font-semibold text-emerald-700">
              {isLoading ? "Carregando..." : error ? "Com problemas" : "Operacional"}
            </p>
            <p className="mt-1 text-xs text-slate-500">
              Dados consultados no backend.
            </p>
          </article>
        </section>

        {error && (
          <div
            role="alert"
            className="mb-6 rounded-lg border border-red-200 bg-red-50 p-4 text-sm text-red-700"
          >
            <p>{error}</p>
            <button
              type="button"
              onClick={loadItems}
              className="mt-2 font-semibold underline"
            >
              Tentar novamente
            </button>
          </div>
        )}

        <div className="grid items-start gap-8 lg:grid-cols-2">
          <section
            aria-labelledby="form-heading"
            className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm"
          >
            <h2 id="form-heading" className="mb-5 text-xl font-bold">
              Novo item
            </h2>
            <ItemForm onAdd={addItem} />
          </section>

          <section
            aria-label="Lista de itens"
            className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm"
          >
            {isLoading ? (
              <p role="status">Carregando itens...</p>
            ) : (
              <ItemList items={items} onDelete={removeItem} />
            )}
          </section>
        </div>

        <footer className="mt-8 text-center text-sm text-slate-500">
          C216 — Projeto acadêmico
        </footer>
      </div>
    </main>
  );
}
