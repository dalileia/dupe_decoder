import { Component, Output, Input } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { Subscription } from 'rxjs';

import { ComparedProductComplete } from '../models/compared.product.complete';
import { ComparedProduct } from '../models/compared.products';
import { Item } from '../models/item.model';
import { Product } from '../models/product.model';
import { HttpService } from '../services/http.service';

@Component({
  selector: 'app-product-detail',
  templateUrl: './product-detail.component.html',
  styleUrls: ['./product-detail.component.css']
})

export class ProductDetailComponent {


  productId: number = 0;
  comparison!: ComparedProductComplete
  product!: Product
  items: Item[] = []
  comparedProduct: ComparedProduct[] = []
  private routeSub: Subscription = new Subscription;
  private productSub: Subscription = new Subscription;

  constructor(
    private activatedRoute: ActivatedRoute,
    private router: Router,
    private dataService: HttpService,
  ) { }

  ngOnInit(id: number) {
    this.routeSub = this.activatedRoute.params.subscribe((params: Params) => {
      this.productId = params['id'];
      this.detailComparedProduct(this.productId);
    });
  }

  detailComparedProduct(search: number) {
    this.productSub = this.dataService
      .compareProduct(search)
      .subscribe((res: any) => {
        this.comparison = res;
        this.product = this.comparison.product
        this.items = this.comparison.product.items
        this.comparison.comparedProducts.map(product => {
          let prod: Product = {
            id: product.product.id,
            name: product.product.name,
            items: product.product.items,
          };
          let result: ComparedProduct = {
            product: prod,
            percentage: product.percentage
          };
          this.comparedProduct.push(result);
        });
      })
    console.log(this.comparedProduct)
  }

  openProduct(id: number) {
    this.comparedProduct = []
    this.detailComparedProduct(id)
  }

  openItem(id: number) {
    this.router.navigate(['items', id]);
  }

  ngOnDestroy() {
    if (this.productSub) {
      this.productSub.unsubscribe();
    }
    if (this.routeSub) {
      this.routeSub.unsubscribe();
    }
  }



}
