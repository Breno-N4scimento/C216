
import { useState } from "react";
import { validateItem } from "../validation";

export function ItemForm({ onAdd }) {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [errors, setErrors] = useState({});
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitError, setSubmitError] = useState("");

  async function handleSubmit(event) {
    event.preventDefault();
    setSubmitError("");

    const item = {
      name: name.trim(),
      description: description.trim(),
    };

    const result = validateItem(item);

    if (result.errors.name) {
      setErrors({ name: result.errors.name });
      return;
    }

    if (result.errors.description) {
      setErrors({ description: result.errors.description });
      return;
    }

    setErrors({});
    setIsSubmitting(true);

    try {
      await onAdd(item);

      setName("");
      setDescription("");
    } catch (error) {
      setSubmitError(
        error.message || "Não foi possível cadastrar o item.",
      );
    } finally {
      setIsSubmitting(false);
    }
  }

  return (
    <form onSubmit={handleSubmit} noValidate className="space-y-4">
      <div>
        <label htmlFor="name" className="mb-1 block text-sm font-medium">
          Nome
        </label>

        <input
          id="name"
          name="name"
          value={name}
          onChange={(event) => setName(event.target.value)}
          className="w-full rounded-lg border border-slate-300 px-3 py-2"
          placeholder="Nome do item"
          disabled={isSubmitting}
        />

        {errors.name && (
          <p role="alert" className="mt-1 text-sm text-red-600">
            {errors.name}
          </p>
        )}
      </div>

      <div>
        <label
          htmlFor="description"
          className="mb-1 block text-sm font-medium"
        >
          Descrição
        </label>

        <textarea
          id="description"
          name="description"
          value={description}
          onChange={(event) => setDescription(event.target.value)}
          className="w-full rounded-lg border border-slate-300 px-3 py-2"
          rows={3}
          placeholder="Descrição do item"
          disabled={isSubmitting}
        />

        {errors.description && (
          <p role="alert" className="mt-1 text-sm text-red-600">
            {errors.description}
          </p>
        )}
      </div>

      {submitError && (
        <p role="alert" className="text-sm text-red-600">
          {submitError}
        </p>
      )}

      <button
        type="submit"
        disabled={isSubmitting}
        className="rounded-lg bg-blue-600 px-4 py-2 font-medium text-white hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-60"
      >
        {isSubmitting ? "Cadastrando..." : "Adicionar"}
      </button>
    </form>
  );
}
