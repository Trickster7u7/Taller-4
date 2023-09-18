package TallerdeDesarrollo.product_microservice.controller;

import TallerdeDesarrollo.product_microservice.entity.ProductEntity;
import TallerdeDesarrollo.product_microservice.repository.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PostMapping;


import java.util.List;

@RestController
@RequestMapping("/api/products")
public class ProductController {
   @Autowired
    private ProductRepository productRepository;
   @GetMapping
   @ResponseStatus(HttpStatus.OK)
   public List<ProductEntity> getAllProducts() {
       return productRepository.findAll();
   }
   @PostMapping
   @ResponseStatus(HttpStatus.OK)
   public void createProduct(ProductEntity ProductEntity){
       productRepository.save(ProductEntity);
   }
}

