
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


# =====================================
# MEMBER 4: MOBILE NAVIGATION MENU
# =====================================

mobile_button = document.getElementById("mobile-menu-btn")
mobile_menu = document.getElementById("mobile-menu")


def toggle_mobile_menu(event):
    mobile_menu.classList.toggle("hidden")

    is_open = not mobile_menu.classList.contains("hidden")
    mobile_button.setAttribute("aria-expanded", str(is_open).lower())


mobile_button.setAttribute("aria-expanded", "false")
mobile_button.addEventListener(
    "click",
    keep(toggle_mobile_menu)
)


# Close the menu after clicking a navigation link.
for link in mobile_menu.querySelectorAll("a"):
    def close_mobile_menu(event):
        mobile_menu.classList.add("hidden")
        mobile_button.setAttribute("aria-expanded", "false")

    link.addEventListener("click", keep(close_mobile_menu))


# =====================================
# MEMBER 5: MODAL OPEN/CLOSE BEHAVIOR
# =====================================

modal = document.getElementById("simple-modal")
modal_title = document.getElementById("modal-title")


def open_modal(title):
    modal_title.textContent = title
    modal.classList.remove("opacity-0", "pointer-events-none")


def close_modal():
    modal.classList.add("opacity-0", "pointer-events-none")


for element in document.querySelectorAll("[data-modal]"):
    title = element.getAttribute("data-modal")

    element.addEventListener(
        "click",
        keep(lambda event, title=title: open_modal(title))
    )


for element in document.querySelectorAll('[data-action="close-modal"]'):
    element.addEventListener(
        "click",
        keep(lambda event: close_modal())
    )


def close_if_backdrop(event):
    if event.target == modal:
        close_modal()


modal.addEventListener("click", keep(close_if_backdrop))


# =====================================
# MEMBER 6: NEWSLETTER AND NOTIFICATIONS
# =====================================

newsletter_form = document.querySelector(
    "#newsletter-email"
).closest("form")


def handle_newsletter(event):
    event.preventDefault()

    show_toast("Thank you for subscribing to our newsletter!")
    newsletter_form.reset()


newsletter_form.addEventListener(
    "submit",
    keep(handle_newsletter)
)
