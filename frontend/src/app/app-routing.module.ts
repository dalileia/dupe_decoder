import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HomeComponent } from './home/home.component';
import { ProductDetailComponent } from './product-detail/product-detail.component';
import { ProductDisplayComponent } from './product-display/product-display.component';
import { ProductSearchComponent } from './product-search/product-search.component';
import { SearchBarComponent } from './search-bar/search-bar.component';

const routes: Routes = [{
  path: '', component: HomeComponent,
},
{
  path: 'home', component: HomeComponent,
},
{
  path: 'search-bar', component: SearchBarComponent,
},
{
  path: 'product-detail/:id', component: ProductDetailComponent,
},
{
  path: 'product-search/:search', component: ProductSearchComponent,
},
{
  path: 'product-display', component: ProductDisplayComponent,
}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
