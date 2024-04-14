<script lang="ts">
  import type { Note } from "$lib/types";
  import Button from "$lib/components/ui/button/button.svelte";
  import ScrollArea from "$lib/components/ui/scroll-area/scroll-area.svelte";
  import NoteItem from "./lib/components/NoteItem.svelte";
  import * as Dialog from "$lib/components/ui/dialog";
  import { Input } from "$lib/components/ui/input";
  import { Textarea } from "$lib/components/ui/textarea";

  let dialogOpen = false;

  let notes: Note[] = [
    {
      id: "1",
      title: "Hello, world!",
      content: "Hello, world!",
      createdAt: new Date(),
    },
    {
      id: "2",
      title: "Hello, world!",
      content: "Hello, Svelte!",
      createdAt: new Date(),
    },
    {
      id: "3",
      title: "Hello, world!",
      content: "Hello, Tailwind CSS!",
      createdAt: new Date(),
    },
    {
      id: "4",
      title: "Hello, world!",
      content: "Hello, world!",
      createdAt: new Date(),
    },
    {
      id: "5",
      title: "Hello, world!",
      content: "Hello, Svelte!",
      createdAt: new Date(),
    },
    {
      id: "6",
      title: "Hello, world!",
      content: "Hello, Tailwind CSS!",
      createdAt: new Date(),
    },
  ];

  let title = "";
  let content = "";

  function addNote() {
    console.log(title, content);
    notes = [
      ...notes,
      {
        id: String(notes.length + 1),
        title: title,
        content: content,
        createdAt: new Date(),
      },
    ];
    clearBindings();
    dialogOpen = false;
  }

  function clearBindings() {
    title = "";
    content = "";
  }
</script>

<main class="*:mx-auto w-screen">
  <div
    class="container bg-stone-100/5 p-14 rounded-xl shadow-xl flex flex-col gap-8 relative"
  >
    <div class="flex items-end justify-between select-none">
      <h1 class="flex items-center justify-center gap-2">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="4rem"
          height="4rem"
          viewBox="0 0 24 24"
          fill="none"
        >
          <path
            d="M9 3V5M12 3V5M15 3V5M13 9H9M15 13H9M8.2 21H15.8C16.9201 21 17.4802 21 17.908 20.782C18.2843 20.5903 18.5903 20.2843 18.782 19.908C19 19.4802 19 18.9201 19 17.8V7.2C19 6.0799 19 5.51984 18.782 5.09202C18.5903 4.71569 18.2843 4.40973 17.908 4.21799C17.4802 4 16.9201 4 15.8 4H8.2C7.0799 4 6.51984 4 6.09202 4.21799C5.71569 4.40973 5.40973 4.71569 5.21799 5.09202C5 5.51984 5 6.07989 5 7.2V17.8C5 18.9201 5 19.4802 5.21799 19.908C5.40973 20.2843 5.71569 20.5903 6.09202 20.782C6.51984 21 7.07989 21 8.2 21Z"
            stroke="#fff"
            stroke-width="1"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
        </svg>
        <span class="text-4xl"> Notes </span>
      </h1>
      <span class="text-3xl text-orange-700">
        {notes.length}
      </span>
    </div>
    <ScrollArea class="h-[60vh] shadow-md flex flex-col gap-2">
      {#each notes as note (note.id)}
        <NoteItem
          {note}
          deleteNote={() => {
            notes = notes.filter((n) => n.id !== note.id);
          }}
        />
      {/each}
    </ScrollArea>
    <Dialog.Root bind:open={dialogOpen}>
      <Dialog.Trigger class="absolute right-0 bottom-0">
        <Button
          class="p-2 w-20 h-20 rounded-lg bg-orange-700 text-5xl shadow-sm shadow-zinc-800 border-2 border-zinc-800 self-center"
        >
          +
        </Button></Dialog.Trigger
      >
      <Dialog.Content class="border-orange-700" on:close={clearBindings}>
        <Dialog.Header>
          <Dialog.Title class="text-2xl">Add New Note</Dialog.Title>
        </Dialog.Header>

        <form class="flex flex-col gap-4" on:submit|preventDefault={addNote}>
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

          <Button
            class="p-4 rounded-xl bg-orange-700 text-lg  shadow-sm shadow-zinc-800 border-2 border-zinc-800"
            type="submit"
          >
            Add Note
          </Button>
        </form>
      </Dialog.Content>
    </Dialog.Root>
  </div>
</main>
