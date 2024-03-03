import { HttpClient } from '@angular/common/http';
import { Component, inject, OnInit } from '@angular/core';

@Component({
  selector: 'app-trade',
  standalone: true,
  imports: [],
  templateUrl: './trade.component.html',
  styleUrl: './trade.component.css'
})
export class TradeComponent implements OnInit{
  http = inject(HttpClient);
  trades: any=[];

  ngOnInit(): void {
    this.fetchTrades();
  }

  fetchTrades(){
    this.http.get('http://localhost:8002/api/trades/all/')
    .subscribe((trades: any) => {
      this.trades = trades;
    })
  }

}
