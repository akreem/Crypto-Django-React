import { HttpClient } from '@angular/common/http';
import { Component, OnInit, inject } from '@angular/core';

@Component({
  selector: 'app-coin',
  standalone: true,
  imports: [],
  templateUrl: './coin.component.html',
  styleUrl: './coin.component.css'
})
export class CoinComponent implements OnInit{

  http = inject(HttpClient);
  coins: any=[];

  ngOnInit(): void {
    this.fetchCoins();
    
  }
  fetchCoins(){
    this.http.get('http://localhost:8002/api/coins/all/')
    .subscribe((coins: any) =>{
        this.coins = coins;
    })
  }
}
