 
    <div class="step">
            <div class="moduleTitle hd">
                    <h2>{$APP.LBL_CR_INVESTOR_PROFILE} - {$APP.LBL_CR_LEGAL_ENTITIES}</h2>
                    <h3>{$APP.LBL_CR_INVESTMENT_GUIDELINES} - {$APP.LBL_CR_STEP} 6</h3>
                    <div class="clear"></div>
            </div>
            <div class="row portfolio-overview">
                    <div class="small-12 column">
                            <p><b>{$APP.LBL_PERCENTAGE_LIQUID_ASSETS}</b><br><br>
                            </p>
                            <form class="step_form">
                                    <p>
    <input type="radio" name="percentage_liquid_assets" value="< 40%" {if $data->percentage_liquid_assets eq "< 40%"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_6_1_TEXT}<br>
    <input type="radio" name="percentage_liquid_assets" value="40% - 70%" {if $data->percentage_liquid_assets eq "40% - 70%"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_6_2_TEXT}<br>
    <input type="radio" name="percentage_liquid_assets" value="> 70%" {if $data->percentage_liquid_assets eq "> 70%"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_6_3_TEXT}<br>
    <input type="radio" name="percentage_liquid_assets" value="nonfound" {if $data->percentage_liquid_assets eq "nonfound"}checked="checked"{/if}>{$APP.LBL_ANSWER_GIIresult_6_4_TEXT}<br>
                                    </p>
                            </form>
                    </div>
            </div>
            <a href="javascript:void(0)" onclick="SUGAR.RiskWorkflow.next()" data-step="7" class="button gen-button next" >{$APP.LBL_CR_NEXT}</a>
    </div> 
