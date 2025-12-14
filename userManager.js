// userManager.js

/**
 * Creates a user profile string
 * @param {object} user - The user object
 * @param {object} config - Configuration options
 */
function createUserProfile(user, config) {
  if (!user.name || !user.email) {
    throw new Error("Invalid user data");
  }

  let role = "Guest";
  // Implicitly requires config to have an optional 'isAdmin' property
  if (config.isAdmin) {
    role = "Admin";
  }

  return {
    id: Date.now(),
    display: "User: " + user.name + " (" + role + ")",
    contact: user.email,
    age: user.age // simple property pass-through
  };
}

function calculateTotal(orders) {
  // Infers 'orders' should be an array of numbers
  return orders.reduce((total, price) => total + price, 0);
}

function getStatus(code) {
  // Returns string or null (Union type needed)
  if (code === 1) return "Active";
  if (code === 2) return "Pending";
  return null;
}

// Example usage that establishes the shape of the objects
const myUser = { name: "Alice", email: "alice@example.com", age: 25 };
const myConfig = { isAdmin: true };
const prices = [10.50, 20.00, 5.25];

const profile = createUserProfile(myUser, myConfig);
const total = calculateTotal(prices);
const status = getStatus(1);

console.log(profile);
console.log("Total Spent:", total);

module.exports = { createUserProfile, calculateTotal, getStatus };
