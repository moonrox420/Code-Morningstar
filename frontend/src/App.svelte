<script lang="ts">
  let prompt = '';
  let response = '';
  async function sendPrompt() {
    const res = await fetch('http://localhost:8000/llm/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt })
    });
    const data = await res.json();
    response = data.result || data.detail || "Error";
  }
</script>

<main>
  <h1>Code Morningstar LLM UI</h1>
  <textarea bind:value={prompt} rows="4" cols="50" placeholder="Enter prompt"></textarea>
  <br />
  <button on:click={sendPrompt}>Send</button>
  <h2>Response:</h2>
  <pre>{response}</pre>
</main>

<style>
  main { padding: 2rem; }
  textarea { width: 100%; }
  button { margin-top: 1rem; }
</style>
