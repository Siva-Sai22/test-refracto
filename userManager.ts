<<<<<<< HEAD
// userManager.ts

interface User {
  name: string;
  email: string;
  age?: number; // 'age' is passed through but not mandatory in the initial check, so make it optional
}

interface Config {
  isAdmin?: boolean; // 'isAdmin' is optional, as it might not be present
}

interface UserProfile {
  id: number;
  display: string;
  contact: string;
  age?: number; // Matches the optionality of User.age
}

function createUserProfile(user: User, config: Config): UserProfile {
=======
// userManager.js

/**
 * Creates a user profile string
 * @param {object} user - The user object
 * @param {object} config - Configuration options
 */
function createUserProfile(user, config) {
>>>>>>> 321f488ced3d98d5c753e92336ee209a1e2ebdee
  if (!user.name || !user.email) {
    throw new Error("Invalid user data");
  }

<<<<<<< HEAD
  let role: "Guest" | "Admin" = "Guest";
=======
  let role = "Guest";
  // Implicitly requires config to have an optional 'isAdmin' property
>>>>>>> 321f488ced3d98d5c753e92336ee209a1e2ebdee
  if (config.isAdmin) {
    role = "Admin";
  }

  return {
    id: Date.now(),
<<<<<<< HEAD
    display: `User: ${user.name} (${role})`,
    contact: user.email,
    age: user.age
  };
}

function calculateTotal(orders: number[]): number {
  return orders.reduce((total, price) => total + price, 0);
}

function getStatus(code: number): string | null {
=======
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
>>>>>>> 321f488ced3d98d5c753e92336ee209a1e2ebdee
  if (code === 1) return "Active";
  if (code === 2) return "Pending";
  return null;
}

// Example usage that establishes the shape of the objects
<<<<<<< HEAD
const myUser: User = { name: "Alice", email: "alice@example.com", age: 25 };
const myConfig: Config = { isAdmin: true };
const prices: number[] = [10.50, 20.00, 5.25];

const profile: UserProfile = createUserProfile(myUser, myConfig);
const total: number = calculateTotal(prices);
const status: string | null = getStatus(1);
=======
const myUser = { name: "Alice", email: "alice@example.com", age: 25 };
const myConfig = { isAdmin: true };
const prices = [10.50, 20.00, 5.25];

const profile = createUserProfile(myUser, myConfig);
const total = calculateTotal(prices);
const status = getStatus(1);
>>>>>>> 321f488ced3d98d5c753e92336ee209a1e2ebdee

console.log(profile);
console.log("Total Spent:", total);

<<<<<<< HEAD
export { createUserProfile, calculateTotal, getStatus };
=======
module.exports = { createUserProfile, calculateTotal, getStatus };
>>>>>>> 321f488ced3d98d5c753e92336ee209a1e2ebdee
