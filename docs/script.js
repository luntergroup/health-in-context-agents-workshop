document.querySelectorAll('.copy-prompt').forEach((button) => {
  button.addEventListener('click', async () => {
    const box = button.closest('.prompt-box');
    const status = box.querySelector('.copy-status');
    try {
      await navigator.clipboard.writeText(box.querySelector('.prompt-text').textContent.trim());
      button.textContent = 'Copied!';
      status.textContent = 'Prompt copied to clipboard.';
      setTimeout(() => { button.textContent = 'Copy prompt'; }, 2500);
    } catch {
      status.textContent = 'Copying was not available. Please select and copy the prompt text.';
      button.textContent = 'Select text to copy';
    }
  });
});
