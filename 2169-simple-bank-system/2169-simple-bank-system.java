class Bank {
    /*
    private long[] balances;
    public Bank(long[] balance) {
        this.balances = balance;
    }
    
    public boolean transfer(int account1, int account2, long money) {
        if(account1 > this.balances.length || account2 > this.balances.length) return false;
        else if(this.balances[account1 - 1] < money) return false;

        this.balances[account1 - 1] -= money;
        this.balances[account2 - 1] += money;

        return true;
    }
    
    public boolean deposit(int account, long money) {
        if(account > this.balances.length) return false;

        this.balances[account - 1] += money;
        return true;
    }
    
    public boolean withdraw(int account, long money) {
        if(account > this.balances.length) return false;
        else if(this.balances[account - 1] < money) return false;

        this.balances[account - 1] -= money;
        return true;
    }
    */

    private long[] balances;
    private int totalAccounts;

    public Bank(long[] balance) {
        this.balances = balance;
        this.totalAccounts = balance.length;
    }
    
    public boolean transfer(int account1, int account2, long money) {
        if(account1 - 1 < this.totalAccounts && account2 - 1 < this.totalAccounts){
            if(this.balances[account1 - 1] >= money){
                this.balances[account1 - 1] -= money;
                this.balances[account2 - 1] += money;

                return true;
            }
        }

        return false;
    }
    
    public boolean deposit(int account, long money) {
        if(account - 1 < this.totalAccounts){
            this.balances[account - 1] += money;
            return true;
        }

        return false;
    }
    
    public boolean withdraw(int account, long money) {
        if(account - 1 < this.totalAccounts && this.balances[account - 1] >= money){
            this.balances[account - 1] -= money;
            return true;
        }

        return false;
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * Bank obj = new Bank(balance);
 * boolean param_1 = obj.transfer(account1,account2,money);
 * boolean param_2 = obj.deposit(account,money);
 * boolean param_3 = obj.withdraw(account,money);
 */