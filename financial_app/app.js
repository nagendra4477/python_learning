// Financial App JavaScript

// Sample Transaction Data
const transactions = [
    {
        id: 1,
        name: "Amazon Shopping",
        category: "shopping",
        icon: "fa-shopping-bag",
        amount: -156.99,
        date: "Today, 2:30 PM"
    },
    {
        id: 2,
        name: "Grocery Store",
        category: "food",
        icon: "fa-shopping-cart",
        amount: -89.50,
        date: "Today, 11:00 AM"
    },
    {
        id: 3,
        name: "Uber Ride",
        category: "transport",
        icon: "fa-car",
        amount: -24.99,
        date: "Yesterday"
    },
    {
        id: 4,
        name: "Netflix Subscription",
        category: "entertainment",
        icon: "fa-play-circle",
        amount: -15.99,
        date: "Mar 9, 2026"
    },
    {
        id: 5,
        name: "Salary Deposit",
        category: "income",
        icon: "fa-briefcase",
        amount: 4500.00,
        date: "Mar 8, 2026"
    }
];

// Chart Data (daily spending for the week)
const chartData = {
    currentWeek: [120, 85, 200, 150, 95, 180, 220],
    previousWeek: [100, 70, 160, 130, 80, 150, 190]
};

// DOM Elements
document.addEventListener('DOMContentLoaded', () => {
    initializeApp();
});

function initializeApp() {
    setCurrentDate();
    renderTransactions();
    renderChart();
    setupEventListeners();
}

// Set Current Date
function setCurrentDate() {
    const dateElement = document.getElementById('currentDate');
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    dateElement.textContent = new Date().toLocaleDateString('en-US', options);
}

// Render Transactions
function renderTransactions() {
    const transactionList = document.getElementById('transactionList');
    transactionList.innerHTML = '';

    transactions.forEach(transaction => {
        const amountClass = transaction.amount > 0 ? 'positive' : 'negative';
        const amountPrefix = transaction.amount > 0 ? '+' : '';
        
        const html = `
            <div class="transaction-item">
                <div class="transaction-left">
                    <div class="transaction-icon ${transaction.category}">
                        <i class="fas ${transaction.icon}"></i>
                    </div>
                    <div class="transaction-details">
                        <h4>${transaction.name}</h4>
                        <span>${transaction.category.charAt(0).toUpperCase() + transaction.category.slice(1)}</span>
                    </div>
                </div>
                <div class="transaction-amount">
                    <div class="amount ${amountClass}">${amountPrefix}$${Math.abs(transaction.amount).toFixed(2)}</div>
                    <div class="date">${transaction.date}</div>
                </div>
            </div>
        `;
        transactionList.innerHTML += html;
    });
}

// Render Chart
function renderChart() {
    const chartContainer = document.getElementById('spendingChart');
    chartContainer.innerHTML = '';

    const maxValue = Math.max(...chartData.currentWeek, ...chartData.previousWeek);

    chartData.currentWeek.forEach((value, index) => {
        const previousValue = chartData.previousWeek[index];
        const currentHeight = (value / maxValue) * 160;
        const previousHeight = (previousValue / maxValue) * 160;

        const html = `
            <div class="bar-group">
                <div class="bar current" style="height: ${currentHeight}px;" title="$${value}"></div>
                <div class="bar previous" style="height: ${previousHeight}px;" title="$${previousValue}"></div>
            </div>
        `;
        chartContainer.innerHTML += html;
    });
}

// Setup Event Listeners
function setupEventListeners() {
    // Transfer Button
    const transferBtn = document.getElementById('transferBtn');
    transferBtn.addEventListener('click', handleTransfer);

    // Notification Button
    const notificationBtn = document.getElementById('notificationBtn');
    notificationBtn.addEventListener('click', () => {
        showToast('You have 3 new notifications');
    });

    // Amount Input - Allow Enter key
    const amountInput = document.getElementById('transferAmount');
    amountInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            handleTransfer();
        }
    });

    // Contact Selection
    const contacts = document.querySelectorAll('.contact');
    contacts.forEach(contact => {
        contact.addEventListener('click', () => {
            contacts.forEach(c => c.style.transform = 'scale(1)');
            contact.style.transform = 'scale(1.1)';
        });
    });
}

// Handle Transfer
function handleTransfer() {
    const amountInput = document.getElementById('transferAmount');
    const amount = parseFloat(amountInput.value);

    if (!amount || amount <= 0) {
        showToast('Please enter a valid amount');
        return;
    }

    if (amount > 5000) {
        showToast('Transfer limit exceeded (Max $5,000)');
        return;
    }

    // Show success message
    const successDiv = document.getElementById('transferSuccess');
    successDiv.classList.add('show');

    // Update total balance
    const balanceElement = document.getElementById('totalBalance');
    const currentBalance = parseFloat(balanceElement.textContent.replace('$', '').replace(',', ''));
    const newBalance = currentBalance - amount;
    balanceElement.textContent = '$' + newBalance.toLocaleString('en-US', { minimumFractionDigits: 2 });

    // Add new transaction
    const newTransaction = {
        id: transactions.length + 1,
        name: "Quick Transfer",
        category: "transfer",
        icon: "fa-paper-plane",
        amount: -amount,
        date: "Just now"
    };
    transactions.unshift(newTransaction);
    renderTransactions();

    // Reset form
    amountInput.value = '';

    // Hide success message after 3 seconds
    setTimeout(() => {
        successDiv.classList.remove('show');
    }, 3000);

    showToast(`Successfully transferred $${amount.toFixed(2)}`);
}

// Show Toast Notification
function showToast(message) {
    const toast = document.getElementById('toast');
    const toastMessage = document.getElementById('toastMessage');
    
    toastMessage.textContent = message;
    toast.classList.add('show');

    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

// Format Currency
function formatCurrency(amount) {
    return '$' + amount.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}
