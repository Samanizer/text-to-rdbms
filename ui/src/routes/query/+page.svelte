<script lang="ts">
    import { page } from '$app/stores';
    
    // Get database details from URL parameters
    $: dbName = $page.url.searchParams.get('dbName') || '';
    $: dbLocation = $page.url.searchParams.get('dbLocation') || '';

    let query = '';
    let results = '';

    function handleAsk() {
        // TODO: Implement actual database query logic
        results = `Query executed: ${query}`;
    }
</script>

<main>
    <div class="container">
        <h1>Talk to your Database</h1>
        
        <section class="db-info">
            <h2>Database Information</h2>
            <p><strong>Name:</strong> {dbName}</p>
            <p><strong>Location:</strong> {dbLocation}</p>
        </section>

        <section class="query-section">
            <h2>Query</h2>
            <textarea bind:value={query} placeholder="Ask a question..."></textarea>
            <button on:click={handleAsk}>Ask</button>
        </section>

        <section class="results-section">
            <h2>Results</h2>
            <div class="results-content">
                {#if results}
                    <pre>{results}</pre>
                {:else}
                    <p>No results yet. Run a query to see results.</p>
                {/if}
            </div>
        </section>
    </div>
</main>

<style>
    :global(body) {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #f5f5f5;
        margin: 0;
        padding: 0;
        color: #333;
    }

    main {
        display: flex;
        justify-content: center;
        padding: 2rem;
    }

    .container {
        background-color: white;
        padding: 2rem;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        width: 100%;
        max-width: 800px;
    }

    h2 {
        color: #2c3e50;
        margin-bottom: 1rem;
    }

    section {
        margin-bottom: 2rem;
    }

    .db-info p {
        margin: 0.5rem 0;
    }

    textarea {
        width: 100%;
        height: 150px;
        padding: 0.5rem;
        border: 1px solid #bdc3c7;
        border-radius: 4px;
        font-size: 1rem;
        margin-bottom: 1rem;
        resize: vertical;
    }

    button {
        background-color: #3498db;
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        font-size: 1rem;
        border-radius: 4px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    button:hover {
        background-color: #2980b9;
    }

    .results-content {
        background-color: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 4px;
        padding: 1rem;
        min-height: 100px;
    }

    pre {
        white-space: pre-wrap;
        word-wrap: break-word;
    }

    h1 {
        text-align: center;
        color: #2c3e50;
        margin-bottom: 1.5rem;
        font-size: 2rem;
    }
</style>
