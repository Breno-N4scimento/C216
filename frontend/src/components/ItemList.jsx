import { useState } from "react";

export function ItemList({ items, onDelete = () => {} }) {
  const [search, setSearch] = useState("");

  const filteredItems = items.filter((item) => {
    const term = search.toLowerCase().trim();

    return (
      item.name.toLowerCase().includes(term) ||
      item.description.toLowerCase().includes(term)
    );
  });

  if (items.length === 0) {
    return <p>Nenhum item cadastrado.</p>;
  }

  return (
    <div className="space-y-4">
      <label htmlFor="item-search" className="sr-only">
        Pesquisar itens
      </label>
      <input
        id="item-search"
        type="search"
        placeholder="Pesquisar itens..."
        value={search}
        onChange={(event) => setSearch(event.target.value)}
        className="w-full rounded-lg border border-slate-300 px-3 py-2"
      />

      {filteredItems.length === 0 ? (
        <p>Nenhum resultado encontrado.</p>
      ) : (
        <ul className="grid gap-3 sm:grid-cols-2">
          {filteredItems.map((item) => (
            <li
              key={item.id}
              className="rounded-xl border border-slate-200 bg-white p-4"
            >
              <h3 className="font-semibold text-slate-900">{item.name}</h3>
              <p className="mt-2 whitespace-pre-wrap text-sm text-slate-600">
                {item.description}
              </p>

              <button
                type="button"
                onClick={() => onDelete(item.id)}
                aria-label={`Excluir ${item.name}`}
                className="mt-4 text-sm text-red-600 hover:underline"
              >
                Excluir
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
