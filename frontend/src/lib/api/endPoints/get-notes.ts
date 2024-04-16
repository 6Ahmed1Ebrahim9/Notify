import type { Note } from "$lib/types";
import { instance } from "../instance";
export const getNotes = async (): Promise<Note[]> => {
  let notes: Note[] = [];
  try {
    const response = await instance.get("notes/");
    return response.data as Note[];
  } catch (error) {
    console.error(error);
  }
  return notes;
};
