<script lang="ts">
	import { goto } from '$app/navigation';

	let dbName = '';
	let dbLocation = '';
	let dbPort = '';
	let dbType = '';
	let dbUsername = '';
	let dbPassword = '';

	function handleSubmit() {
		// Navigate to the query page with database details as URL parameters
		goto(`/query?dbName=${encodeURIComponent(dbName)}&dbLocation=${encodeURIComponent(dbLocation)}`);
	}
</script>

<main>
	<div class="container">
		<h1>Database Connection</h1>
		<form on:submit|preventDefault={handleSubmit}>
			<div class="form-group">
				<label for="dbName">Database Name</label>
				<input id="dbName" type="text" bind:value={dbName} required>
			</div>

			<div class="form-group">
				<label for="dbLocation">Location</label>
				<input id="dbLocation" type="text" bind:value={dbLocation} required>
			</div>

			<div class="form-group">
				<label for="dbPort">Port</label>
				<input id="dbPort" type="number" bind:value={dbPort} required>
			</div>

			<div class="form-group">
				<label for="dbType">Database Type</label>
				<select id="dbType" bind:value={dbType} required>
					<option value="">Select a database type</option>
					<option value="mysql">MySQL</option>
					<option value="postgresql">PostgreSQL</option>
					<option value="mongodb">MongoDB</option>
				</select>
			</div>

			<div class="form-group">
				<label for="dbUsername">Username</label>
				<input id="dbUsername" type="text" bind:value={dbUsername} required>
			</div>

			<div class="form-group">
				<label for="dbPassword">Password</label>
				<input id="dbPassword" type="password" bind:value={dbPassword} required>
			</div>

			<button type="submit">Connect</button>
		</form>
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
		align-items: center;
		min-height: 100vh;
	}

	.container {
		background-color: white;
		padding: 2rem;
		border-radius: 8px;
		box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
		width: 100%;
		max-width: 400px;
	}

	h1 {
		text-align: center;
		color: #2c3e50;
		margin-bottom: 1.5rem;
	}

	form {
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}

	.form-group {
		display: flex;
		flex-direction: column;
	}

	label {
		margin-bottom: 0.5rem;
		font-weight: 600;
		color: #34495e;
	}

	input, select {
		padding: 0.5rem;
		border: 1px solid #bdc3c7;
		border-radius: 4px;
		font-size: 1rem;
		transition: border-color 0.3s ease;
	}

	input:focus, select:focus {
		outline: none;
		border-color: #3498db;
	}

	button {
		background-color: #3498db;
		color: white;
		border: none;
		padding: 0.75rem;
		font-size: 1rem;
		border-radius: 4px;
		cursor: pointer;
		transition: background-color 0.3s ease;
	}

	button:hover {
		background-color: #2980b9;
	}
</style>
