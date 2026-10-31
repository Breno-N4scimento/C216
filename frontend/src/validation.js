export function validateItem({ name, description }) {
  const errors = {};

  if (!name?.trim()) {
    errors.name = "O nome é obrigatório.";
  }

  if (!description?.trim()) {
    errors.description = "A descrição é obrigatória.";
  }

  return { errors };
}
