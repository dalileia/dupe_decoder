import { Component, Input, Output, EventEmitter } from '@angular/core';
import { Product } from '../models/product.model';

@Component({
  selector: 'app-product-display',
  templateUrl: './product-display.component.html',
  styleUrls: ['./product-display.component.css']
})
export class ProductDisplayComponent {

  @Input() product!: Product;
  @Input() percentage: number = 0

  @Output() messageEvent = new EventEmitter<number>();

  sendMessage(id: number) {
    this.messageEvent.emit(id)
  }

}
