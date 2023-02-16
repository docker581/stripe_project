const data = document.currentScript.dataset;
const order_id = data.id;
const url = "/buy/" + order_id
// console.log(url)
document.querySelector("#submitBtn").addEventListener("click", () => {
    fetch(url)
    .then((result) => { return result.json(); })
    .then((data) => {
        // console.log(data);
        const stripe = Stripe(data.publicKey);
        return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
});
