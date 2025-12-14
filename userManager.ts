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
  if (!user.name || !user.email) {
    throw new Error("Invalid user data");
  }

  let role: "Guest" | "Admin" = "Guest";
  if (config.isAdmin) {
    role = "Admin";
  }

  return {
    id: Date.now(),
    display: `User: ${user.name} (${role})`,
    contact: user.email,
    age: user.age
  };
}

function calculateTotal(orders: number[]): number {
  return orders.reduce((total, price) => total + price, 0);
}

function getStatus(code: number): string | null {
  if (code === 1) return "Active";
  if (code === 2) return "Pending";
  return null;
}

// Example usage that establishes the shape of the objects
const myUser: User = { name: "Alice", email: "alice@example.com", age: 25 };
const myConfig: Config = { isAdmin: true };
const prices: number[] = [10.50, 20.00, 5.25];

const profile: UserProfile = createUserProfile(myUser, myConfig);
const total: number = calculateTotal(prices);
const status: string | null = getStatus(1);

console.log(profile);
console.log("Total Spent:", total);

export { createUserProfile, calculateTotal, getStatus };