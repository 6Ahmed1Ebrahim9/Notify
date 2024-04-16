import type { Note } from "$lib/types";
import { instance } from "../instance";
export const createNote = async (note: Note) => {
  try {
    const response = await instance.put(`notes/${note.id}/update`, {
      title: note.title,
      content: note.content,
    });
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
