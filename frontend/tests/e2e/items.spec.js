import { expect, test } from "@playwright/test";

test("cadastra um item e o exibe na listagem", async ({ page }) => {
  await page.goto("/");

  await page.getByLabel("Nome").fill("Notebook");
  await page.getByLabel("Descrição").fill("14 polegadas");
  await page.getByRole("button", { name: "Adicionar" }).click();

  await expect(page.getByRole("listitem")).toContainText("Notebook");
  await expect(page.getByText("Nenhum item cadastrado.")).toBeHidden();
});
