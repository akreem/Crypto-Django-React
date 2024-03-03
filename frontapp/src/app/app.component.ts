import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CoinComponent } from './coin/coin.component';
import { TradeComponent } from './trade/trade.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CoinComponent, TradeComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'frontapp';
}
