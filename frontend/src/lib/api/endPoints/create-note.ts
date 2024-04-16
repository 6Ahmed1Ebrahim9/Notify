import type { Note } from "../../types";
import { instance } from "../instance";
export const createNote = async (note: {
  title: string;
  content: string;
}): Promise<Note | null> => {
  let newNote: Note | null = null;
  try {
    const response = await instance.post("notes/create/", note);
    newNote = response.data;
  } catch (error) {
    console.error(error);
  }
  return newNote;
};
