<script lang="ts">
  import type { Note } from "../types";
  import * as Dialog from "./ui/dialog";
  import { Button } from "./ui/button";
  import { Input } from "./ui/input";
  import { Textarea } from "./ui/textarea";
  export let note: Note;
  export let deleteNote: () => void;

  note.createdAt = new Date(note.createdAt.split(":")[0])?.toISOString();

  let title = note.title;
  let content = note.content;

  let isEditMode = false;

  function updateNote(title: string, content: string | null) {
    note = { ...note, title, content };
  }
</script>

<Dialog.Root>
  <Dialog.Trigger class="w-full">
    <div
      class="flex flex-col gap-4 bg-stone-900 p-6 overflow-ellipsis rounded-lg hover:bg-orange-800 cursor-pointer group/taskItem transition-all ease-in-out"
    >
      <h2 class="text-3xl">
        {note.title}
      </h2>
      <div
        class="flex gap-2 *:text-xl *:text-zinc-400 *:group-hover/taskItem:text-zinc-200 transition-all ease-in"
      >
        <span>
          {note.createdAt}
        </span>
        {#if note.content}
          <span> - </span>
          <span>
            {note.content}
          </span>
        {/if}
      </div>
    </div>
  </Dialog.Trigger>
  <Dialog.Content
    class="border-orange-700"
    on:close={() => {
      isEditMode = false;
    }}
  >
    <Dialog.Header>
      <Dialog.Title class="text-2xl">
        <div class="flex gap-2 items-end">
          <span class="text-3xl">
            {note.title}
          </span>
          <span class="space-x-1">
            <Button
              variant="ghost"
              class="hover:bg-zinc-500 h-fit px-2 py-2  my-0.5 w-fit"
              on:click={() => {
                isEditMode = !isEditMode;
              }}
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="1.2rem"
                height="1.2rem"
                viewBox="0 0 24 24"
                fill="none"
              >
                <path
                  d="M20.1497 7.93997L8.27971 19.81C7.21971 20.88 4.04971 21.3699 3.27971 20.6599C2.50971 19.9499 3.06969 16.78 4.12969 15.71L15.9997 3.84C16.5478 3.31801 17.2783 3.03097 18.0351 3.04019C18.7919 3.04942 19.5151 3.35418 20.0503 3.88938C20.5855 4.42457 20.8903 5.14781 20.8995 5.90463C20.9088 6.66146 20.6217 7.39189 20.0997 7.93997H20.1497Z"
                  stroke="#fff"
                  stroke-width="1.5"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
                <path
                  d="M21 21H12"
                  stroke="#fff"
                  stroke-width="1.5"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </svg>
            </Button>
            <Button
              class="hover:bg-red-800 h-fit px-2 py-2  my-0.5 w-fit group/delBtn"
              variant="ghost"
              on:click={() => {
                deleteNote();
              }}
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="1.2rem"
                height="1.2rem"
                viewBox="0 0 1024 1024"
                class="[&_path]:fill-red-700 group-hover/delBtn:[&_path]:fill-zinc-200"
                ><path
                  d="M160 256H96a32 32 0 0 1 0-64h256V95.936a32 32 0 0 1 32-32h256a32 32 0 0 1 32 32V192h256a32 32 0 1 1 0 64h-64v672a32 32 0 0 1-32 32H192a32 32 0 0 1-32-32V256zm448-64v-64H416v64h192zM224 896h576V256H224v640zm192-128a32 32 0 0 1-32-32V416a32 32 0 0 1 64 0v320a32 32 0 0 1-32 32zm192 0a32 32 0 0 1-32-32V416a32 32 0 0 1 64 0v320a32 32 0 0 1-32 32z"
                /></svg
              >
            </Button>
          </span>
        </div>
      </Dialog.Title>
    </Dialog.Header>

    {#if isEditMode}
      <form class="flex flex-col gap-4">
        <fieldset class="flex flex-col">
          <label for="noteTitle" class="sr-only"> Title </label>
          <Input
            type="text"
            name="noteTitle"
            class="p-4 rounded-xl bg-stone-100/5"
            placeholder="Title"
            bind:value={title}
          />
        </fieldset>
        <fieldset class="flex flex-col">
          <label for="noteContent" class="sr-only"> Content </label>
          <Textarea
            name="noteContent"
            class="p-4 rounded-xl bg-stone-100/5"
            placeholder="Content"
            bind:value={content}
          />
        </fieldset>
        <div class="*:w-full flex gap-2 items-center">
          <Button
            class="p-4 rounded-xl hover:bg-orange-500 text-lg  shadow-sm shadow-zinc-800 border-2 border-zinc-800"
            variant="outline"
            type="button"
            on:click={() => {
              isEditMode = false;
            }}
          >
            Cancel
          </Button>

          <Button
            class="p-4 rounded-xl bg-orange-700 text-lg  shadow-sm shadow-zinc-800 border-2 border-zinc-800 hover:bg-orange-800"
            type="submit"
            on:click={() => {
              updateNote(title, content);
              isEditMode = false;
            }}
          >
            Save
          </Button>
        </div>
      </form>
    {:else}
      <div class="flex flex-col gap-4">
        <span class="text-2xl">{note.content}</span>
      </div>
      <span class=" text-zinc-400">
        {Date.parse(note.createdAt)}
      </span>
    {/if}
  </Dialog.Content>
</Dialog.Root>
