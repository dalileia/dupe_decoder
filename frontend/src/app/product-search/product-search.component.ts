import { Component, Input } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { Subscription } from 'rxjs';

import { Item } from '../models/item.model';
import { Product } from '../models/product.model';
import { HttpService } from '../services/http.service';

@Component({
  selector: 'app-product-search',
  templateUrl: './product-search.component.html',
  styleUrls: ['./product-search.component.css']
})
export class ProductSearchComponent {

  search: any;
  public products: Product[] = []
  items: Item[] = []
  private routeSub: Subscription = new Subscription;
  private homeSub: Subscription = new Subscription;

  constructor(
    private dataService: HttpService,
    private router: Router,
    private activatedRoute: ActivatedRoute) { }

  ngOnInit() {
    this.routeSub = this.activatedRoute.params.subscribe((params: Params) => {
      this.search = params['search'];
      this.searchProducts(this.search);
    });
  }

  searchProducts(search: any) {
    this.homeSub = this.dataService
      .productSearch(search)
      .subscribe((res: any) => {
        this.products = res;
        console.log(this.products)
      });
  }

  openProduct(id: number) {
    this.router.navigate(['product-detail', id]);
  }

  ngOnDestroy(): void {
    if (this.homeSub) {
      this.homeSub.unsubscribe();
    }

    if (this.routeSub) {
      this.routeSub.unsubscribe();
    }
  }
}
