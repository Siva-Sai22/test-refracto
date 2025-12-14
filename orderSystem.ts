/**
 * Represents the possible statuses an order can have.
 */
type OrderStatus = "shipped" | "pending" | "delivered";

/**
 * Interface for a customer associated with an order.
 */
interface ICustomer {
  name: string;
  email: string;
  isVIP?: boolean; // isVIP is optional
}

/**
 * Interface for an individual order.
 */
interface IOrder {
  id: number;
  amount: number;
  status: OrderStatus;
  customer?: ICustomer; // customer is optional
}

const API_DATA: IOrder[] = [
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

function calculateRevenue(orders: IOrder[]): number {
  return orders.reduce((total, order) => {
    return total + order.amount;
  }, 0);
}

function filterByStatus(orders: IOrder[], status: OrderStatus): IOrder[] {
  return orders.filter(o => o.status === status);
}

function sendEmail(order: IOrder): boolean {
  // Robustly check if customer and email exist before attempting to use them
  if (order.customer?.email) {
    const address = order.customer.email;
    console.log(`Sending email to ${address} for Order #${order.id}`);
    return true;
  }
  console.log(`Could not send email for Order #${order.id}: No customer email address found.`);
  return false;
}

const total: number = calculateRevenue(API_DATA);
const pendingOrders: IOrder[] = filterByStatus(API_DATA, "pending");

console.log("Total Revenue: $" + total.toFixed(2));

API_DATA.forEach((order: IOrder) => {
  // The original JS condition 'order.status !== "pending"'
  // *coincidentally* prevented calling sendEmail for the order without a customer.
  // With the robust sendEmail function, we can still keep this condition
  // if the intent is only to send emails for non-pending orders.
  if (order.status !== "pending") {
    sendEmail(order); // sendEmail now handles cases where customer/email might be missing
  }
});

export { calculateRevenue, filterByStatus };