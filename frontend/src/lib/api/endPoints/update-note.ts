import type { Note } from "$lib/types";
import { instance } from "../instance";
export const updateNote = async (note: Note): Promise<Note | null> => {
  let updatedNote: Note | null = null;
  try {
    const response = await instance.put(`notes/${note.id}/update`, {
      title: note.title,
      content: note.content,
    });
    updatedNote = response.data;
  } catch (error) {
    console.error(error);
  }
  return updatedNote;
};
