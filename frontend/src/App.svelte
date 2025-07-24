<script lang="ts">
  import { onMount } from 'svelte';

  let prompt = '';
  let response = '';
  let loading = false;
  let healthStatus = 'Checking...';

  const checkHealth = async () => {
    try {
      const res = await fetch('/api/llm/health');
      const data = await res.json();
      healthStatus = data.status === 'healthy' ? 'Healthy' : 'Unhealthy';
    } catch (error) {
      healthStatus = 'Error';
    }
  };

  const generateResponse = async () => {
    if (!prompt.trim()) return;
    
    loading = true;
    try {
      const res = await fetch('/api/llm/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          prompt: prompt,
          max_tokens: 100
        })
      });
      const data = await res.json();
      response = data.response || 'No response received';
    } catch (error) {
      response = 'Error: ' + error.message;
    } finally {
      loading = false;
    }
  };

  onMount(() => {
    checkHealth();
  });
</script>

<main>
  <div class="container">
    <header>
      <h1>🌟 Code Morningstar</h1>
      <p class="subtitle">Local LLM Code Assistant</p>
      <div class="health-status">
        Status: <span class="status-{healthStatus.toLowerCase()}">{healthStatus}</span>
      </div>
    </header>

    <div class="chat-container">
      <div class="input-section">
        <textarea 
          bind:value={prompt}
          placeholder="Enter your code prompt here..."
          disabled={loading}
          on:keydown={(e) => {
            if (e.key === 'Enter' && e.ctrlKey) {
              generateResponse();
            }
          }}
        ></textarea>
        <button 
          on:click={generateResponse}
          disabled={loading || !prompt.trim()}
          class="generate-btn"
        >
          {loading ? 'Generating...' : 'Generate (Ctrl+Enter)'}
        </button>
      </div>

      {#if response}
        <div class="response-section">
          <h3>Response:</h3>
          <pre class="response-text">{response}</pre>
        </div>
      {/if}
    </div>
  </div>
</main>

<style>
  :global(body) {
    margin: 0;
    padding: 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
  }

  .container {
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }

  header {
    text-align: center;
    margin-bottom: 2rem;
    color: white;
  }

  h1 {
    font-size: 3rem;
    margin: 0;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
  }

  .subtitle {
    font-size: 1.2rem;
    margin: 0.5rem 0;
    opacity: 0.9;
  }

  .health-status {
    margin-top: 1rem;
    font-weight: bold;
  }

  .status-healthy { color: #4CAF50; }
  .status-unhealthy { color: #f44336; }
  .status-error { color: #ff9800; }
  .status-checking { color: #2196F3; }

  .chat-container {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 15px;
    padding: 2rem;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    flex: 1;
  }

  .input-section {
    margin-bottom: 1.5rem;
  }

  textarea {
    width: 100%;
    min-height: 120px;
    padding: 1rem;
    border: 2px solid #ddd;
    border-radius: 8px;
    font-size: 1rem;
    resize: vertical;
    font-family: 'Courier New', monospace;
    margin-bottom: 1rem;
    box-sizing: border-box;
  }

  textarea:focus {
    border-color: #667eea;
    outline: none;
  }

  .generate-btn {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 8px;
    font-size: 1rem;
    cursor: pointer;
    transition: transform 0.2s;
  }

  .generate-btn:hover:not(:disabled) {
    transform: translateY(-2px);
  }

  .generate-btn:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }

  .response-section {
    border-top: 2px solid #eee;
    padding-top: 1.5rem;
  }

  .response-text {
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 8px;
    padding: 1rem;
    white-space: pre-wrap;
    font-family: 'Courier New', monospace;
    max-height: 400px;
    overflow-y: auto;
  }

  h3 {
    margin-top: 0;
    color: #333;
  }
</style>