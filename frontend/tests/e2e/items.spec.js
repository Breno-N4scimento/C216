import { expect, test } from "@playwright/test";

test("cadastra um item e mantém os dados após recarregar a página", async ({
  page,
}) => {
  await page.goto("http://localhost:8080");

  const nome = `Notebook-${Date.now()}`;

  await page.getByLabel("Nome").fill(nome);
  await page.getByLabel("Descrição").fill("14 polegadas");

  await page.getByRole("button", { name: "Adicionar" }).click();

  await expect(page.getByRole("alert")).not.toBeVisible();

  await expect(page.getByText(nome, { exact: true })).toBeVisible({
    timeout: 10000,
  });

  await page.reload();

  await expect(page.getByText(nome, { exact: true })).toBeVisible({
    timeout: 10000,
  });
});
