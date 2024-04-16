import { instance } from "../instance";
export const createNote = async (noteId: number) => {
  try {
    const response = await instance.delete(`notes/${noteId}/delete`);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
