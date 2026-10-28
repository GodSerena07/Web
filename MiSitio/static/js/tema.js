document.addEventListener("DOMContentLoaded", function () {
    const botonTema = document.getElementById("boton-tema");
    const iconoTema = document.getElementById("icono-tema");
    const textoTema = document.getElementById("texto-tema");

    if (!botonTema || !iconoTema || !textoTema) {
        return;
    }

    // Recuperar el tema guardado o utilizar el tema claro.
    const temaGuardado = localStorage.getItem("tema") || "light";

    aplicarTema(temaGuardado);

    // Cambiar el tema cuando se pulsa el botón.
    botonTema.addEventListener("click", function () {
        const temaActual = document.documentElement.dataset.theme;
        const nuevoTema = temaActual === "dark" ? "light" : "dark";

        aplicarTema(nuevoTema);

        // Guardar la preferencia para las otras páginas.
        localStorage.setItem("tema", nuevoTema);
    });

    function aplicarTema(tema) {
        document.documentElement.dataset.theme = tema;

        if (tema === "dark") {
            iconoTema.textContent = "☀️";
            textoTema.textContent = "Tema claro";
            botonTema.setAttribute("aria-pressed", "true");
        } else {
            iconoTema.textContent = "🌙";
            textoTema.textContent = "Tema oscuro";
            botonTema.setAttribute("aria-pressed", "false");
        }
    }
});
