// Auto-dismiss alerts after 5 seconds
document.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
        document.querySelectorAll('.alert-dismissible').forEach(el => {
            const btn = el.querySelector('.btn-close');
            if (btn) btn.click();
        });
    }, 5000);
});