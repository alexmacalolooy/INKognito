from pyscript import document, ffi
from js import setTimeout

# Keep event callback proxies alive while the page is open.
_callbacks = []

def keep(callback):
    proxy = ffi.create_proxy(callback)
    _callbacks.append(proxy)
    return proxy

def show_toast(message):
    toast = document.getElementById("toast")
    toast_message = document.getElementById("toast-message")
    toast_message.textContent = message
    toast.classList.remove("translate-y-32", "opacity-0")
    toast.classList.add("translate-y-0", "opacity-100")

    def hide_toast():
        toast.classList.remove("translate-y-0", "opacity-100")
        toast.classList.add("translate-y-32", "opacity-0")

    setTimeout(keep(hide_toast), 4000)

# Mobile navigation menu
mobile_button = document.getElementById("mobile-menu-btn")
mobile_menu = document.getElementById("mobile-menu")
mobile_button.addEventListener(
    "click",
    keep(lambda event: mobile_menu.classList.toggle("hidden"))
)

# Modal open/close behavior
modal = document.getElementById("simple-modal")
modal_title = document.getElementById("modal-title")

def open_modal(title):
    modal_title.textContent = title
    modal.classList.remove("opacity-0", "pointer-events-none")

def close_modal():
    modal.classList.add("opacity-0", "pointer-events-none")

for element in document.querySelectorAll("[data-modal]"):
    title = element.getAttribute("data-modal")
    element.addEventListener("click", keep(lambda event, title=title: open_modal(title)))

for element in document.querySelectorAll('[data-action="close-modal"]'):
    element.addEventListener("click", keep(lambda event: close_modal()))

def close_if_backdrop(event):
    if event.target == modal:
        close_modal()

modal.addEventListener("click", keep(close_if_backdrop))

# Newsletter form: preserve the original success message and reset behavior.
newsletter_form = document.querySelector("#newsletter-email").closest("form")

def handle_newsletter(event):
    event.preventDefault()
    show_toast("Thank you for subscribing to our newsletter!")
    newsletter_form.reset()

newsletter_form.addEventListener("submit", keep(handle_newsletter))
