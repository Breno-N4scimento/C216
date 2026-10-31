import { useState } from "react";
import { ItemForm } from "./components/ItemForm";
import { ItemList } from "./components/ItemList";

export default function App() {
  const [items, setItems] = useState([]);

  function addItem({ name, description }) {
    const newItem = {
      id: `${Date.now()}-${Math.random()}`,
      name,
      description,
    };

    setItems((currentItems) => [newItem, ...currentItems]);
  }

  function deleteItem(id) {
    setItems((currentItems) => currentItems.filter((item) => item.id !== id));
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
              Operacional
            </p>
            <p className="mt-1 text-xs text-slate-500">
              Dados mantidos temporariamente nesta sessão.
            </p>
          </article>
        </section>

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
            <ItemList items={items} onDelete={deleteItem} />
          </section>
        </div>

        <footer className="mt-8 text-center text-sm text-slate-500">
          C216 — Projeto acadêmico
        </footer>
      </div>
    </main>
  );
}
