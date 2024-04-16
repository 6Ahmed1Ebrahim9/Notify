import { instance } from "../instance";
export const deleteNote = async (noteId: number): Promise<boolean> => {
  const response = await instance.delete(`notes/${noteId}/delete`);
  return response.status === 200 ? true : false;
};
