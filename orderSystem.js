const API_DATA = [
  {
    id: 101,
    amount: 150.00,
    status: "shipped",
    customer: { name: "Alice", email: "alice@example.com" }
  },
  {
    id: 102,
    amount: 45.50,
    status: "pending",
  },
  {
    id: 103,
    amount: 200.00,
    status: "delivered",
    customer: { name: "Bob", email: "bob@test.com", isVIP: true }
  }
];

function calculateRevenue(orders) {
  return orders.reduce((total, order) => {
    return total + order.amount;
  }, 0);
}

function sendEmail(order) {
  const address = order.customer.email;
  
  console.log("Sending email to " + address + " for Order #" + order.id);
  return true;
}

function filterByStatus(orders, status) {
  return orders.filter(o => o.status === status);
}

const total = calculateRevenue(API_DATA);
const pendingOrders = filterByStatus(API_DATA, "pending");

console.log("Total Revenue: $" + total.toFixed(2));

API_DATA.forEach(order => {
  if (order.status !== "pending") {
    sendEmail(order);
  }
});

module.exports = { calculateRevenue, filterByStatus };
