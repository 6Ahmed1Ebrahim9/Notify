import { instance } from "../instance";
export const createNote = async (note: { title: string; content: string }) => {
  try {
    const response = await instance.post("notes/create/", note);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
