/*
  Warnings:

  - A unique constraint covering the columns `[text]` on the table `Url` will be added. If there are existing duplicate values, this will fail.

*/
-- CreateIndex
CREATE UNIQUE INDEX "Url_text_key" ON "Url"("text");
