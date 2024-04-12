<script lang="ts">
  import type { Note } from "../types";

  export let note: Note;
</script>

<main class="flex flex-col gap-4 bg-stone-900 p-6 overflow-ellipsis rounded-lg">
  <h2 class="text-3xl">
    {note.title}
  </h2>
  <div class="flex gap-2 *:text-xl *:text-zinc-400">
    <span>
      {note.createdAt.toLocaleDateString()}
    </span>
    {#if note.content}
      <span> - </span>
      <span>
        {note.content}
      </span>
    {/if}
  </div>
</main>
